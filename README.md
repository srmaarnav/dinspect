# DoInspect - Docker Container Inspector

`cinspect` is a command-line tool to inspect running Docker containers, including:
- Environment Variables
- Network Usage
- Port Mappings
- Volume Mappings

## Installation
```bash
pip install cinspect
```

## Usage

```
cinspect -c my_container   # Inspect all details
cinspect -c my_container -e  # Show environment variables
cinspect -c my_container -n  # Show network usage
```

## License

MIT License

