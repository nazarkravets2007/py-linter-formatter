def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "column": error["column"],
        "message": error["message"],
        "name": error["code"],
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "filePath": file_path,
        "messages": [format_linter_error(error) for error in errors],
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
