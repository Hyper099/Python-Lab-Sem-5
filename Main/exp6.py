
class FileNotFoundCustomError(Exception):
    pass

class InvalidInputDataError(Exception):
    pass

class DiskSpaceFullError(Exception):
    pass


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        if not isinstance(data, str):
            raise InvalidInputDataError("The file contains non-text data.")
        return data
    except FileNotFoundError:
        raise FileNotFoundCustomError(f"Error: The file '{file_path}' was not found.")
    except UnicodeDecodeError:
        raise InvalidInputDataError("File contains invalid characters or encoding issues.")


def process_text(data):
    if not isinstance(data, str) or data.strip() == "":
        raise InvalidInputDataError("Invalid or empty text data provided.")

    words = data.split()
    word_count = len(words)

    char_frequency = {}
    for char in data:
        if char.isalpha():  
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1

    return {
        "word_count": word_count,
        "char_frequency": char_frequency
    }


def write_output(output_path, results):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=== Text Processing Results ===\n")
            f.write(f"Total Words: {results['word_count']}\n")
            f.write("\nCharacter Frequencies:\n")
            for char, freq in sorted(results['char_frequency'].items()):
                f.write(f"{char}: {freq}\n")
    except OSError as e:
        raise DiskSpaceFullError(f"Disk space full or unable to write to '{output_path}'. Error: {str(e)}")


def main():
    print("=== Python Text Processing Tool ===")
    input_file = input("Enter the input file path: ").strip()
    output_file = input("Enter the output file path: ").strip()

    try:
        content = read_file(input_file)

        results = process_text(content)

        write_output(output_file, results)
        print(f"Processing complete! Results saved to '{output_file}'.")

    except (FileNotFoundCustomError, InvalidInputDataError, DiskSpaceFullError) as e:
        print(f"[ERROR]: {e}")
    except Exception as e:
        print(f"[UNEXPECTED ERROR]: {str(e)}")


if __name__ == "__main__":
    main()