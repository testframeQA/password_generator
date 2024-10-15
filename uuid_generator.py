import argparse
import uuid

def generate_uuid() -> uuid.UUID:
    unique_uuid = uuid.uuid4()
    print(f"UUID: {unique_uuid}")

    return unique_uuid

if __name__ == "__main__":
    generate_uuid()
