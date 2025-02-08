# Image Organization Tool

A Python tool to organize and identify similar images in your collection.

## Directory Structure

```
project/
├── main.py
├── png/          # Directory for downloaded images
└── output/       # Directory for similar images
```

## Usage

1. Place your downloaded images in the `png` directory

2. Run the script:
   ```bash
   python3 -m main
   ```

3. Results:
   - Similar images will be automatically processed and stored in the `output` directory
   - Each group of similar images will be organized in separate subdirectories

## Notes

- Ensure all images are in PNG format
- The tool will automatically create the output directory if it doesn't exist
- Original images in the `png` directory remain unchanged