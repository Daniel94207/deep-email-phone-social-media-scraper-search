thonimport argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List

from core.crawler import Crawler

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger("deep_contact_scraper")

def resolve_base_dir() -> Path:
    """
    Resolve the project root directory based on this file's location.
    Assumes this file lives in <root>/src/main.py.
    """
    return Path(__file__).resolve().parent.parent

def load_settings(config_path: Path) -> Dict[str, Any]:
    if not config_path.exists():
        logger.error("Settings file not found at %s", config_path)
        raise FileNotFoundError(f"Settings file not found: {config_path}")
    try:
        with config_path.open("r", encoding="utf-8") as f:
            settings = json.load(f)
        logger.debug("Loaded settings: %s", settings)
        return settings
    except json.JSONDecodeError as e:
        logger.exception("Failed to parse settings.json")
        raise ValueError(f"Invalid JSON in settings file: {e}") from e

def load_input_urls(path: Path) -> List[str]:
    if not path.exists():
        logger.error("Input URL file not found at %s", path)
        raise FileNotFoundError(f"Input URL file not found: {path}")

    urls: List[str] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)

    if not urls:
        logger.warning("No URLs found in %s", path)
    else:
        logger.info("Loaded %d URLs from %s", len(urls), path)
    return urls

def save_results(results: List[Dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        logger.info("Saved %d result records to %s", len(results), path)
    except OSError:
        logger.exception("Failed to write results to %s", path)
        raise

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Deep Email, Phone, & Social Media Scraper Search"
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to settings.json (default: src/config/settings.json)",
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Optional override for input URLs file",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional override for output JSON file",
    )
    parser.add_argument(
        "--max-sites",
        type=int,
        default=None,
        help="Optionally limit the number of sites to process from input list",
    )
    return parser.parse_args(argv)

def main(argv: List[str]) -> int:
    base_dir = resolve_base_dir()
    args = parse_args(argv)

    config_path = Path(args.config) if args.config else base_dir / "src" / "config" / "settings.json"

    try:
        settings = load_settings(config_path)
    except Exception as exc:  # noqa: BLE001
        logger.error("Failed to load configuration: %s", exc)
        return 1

    input_path = Path(args.input) if args.input else base_dir / settings.get(
        "input_file", "data/input_urls.txt"
    )
    output_path = Path(args.output) if args.output else base_dir / settings.get(
        "output_file", "data/results_sample.json"
    )

    try:
        urls = load_input_urls(input_path)
    except Exception as exc:  # noqa: BLE001
        logger.error("Failed to load input URLs: %s", exc)
        return 1

    if args.max-sites is not None:
        urls = urls[: args.max-sites]

    if not urls:
        logger.error("No URLs to scrape. Exiting.")
        return 1

    logger.info("Starting crawl for %d websites", len(urls))
    crawler = Crawler(settings=settings)

    try:
        results = crawler.crawl(urls)
    except KeyboardInterrupt:
        logger.warning("Interrupted by user, partial results may be incomplete.")
        return 1
    except Exception as exc:  # noqa: BLE001
        logger.exception("Unexpected error during crawl: %s", exc)
        return 1

    try:
        save_results(results, output_path)
    except Exception as exc:  # noqa: BLE001
        logger.error("Failed to save results: %s", exc)
        return 1

    logger.info("Crawl finished successfully.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))