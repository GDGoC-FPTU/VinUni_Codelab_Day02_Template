#!/usr/bin/env python3
"""Run the Xanh SM low-battery dispatch co-pilot in a terminal."""

from __future__ import annotations

import argparse

from xanhsm_dispatch.chat import TerminalChat


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Chat điều phối sự cố pin Xanh SM")
    parser.add_argument("--offline", action="store_true", help="Không gọi Gemini; dùng kết quả tất định")
    parser.add_argument("--data-dir", help="Thư mục chứa vehicle_specs.json và charging_stations.json")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    TerminalChat(data_dir=args.data_dir, offline=args.offline).run()


if __name__ == "__main__":
    main()
