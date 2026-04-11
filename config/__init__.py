import os
import yaml

_config = None


def get_config():
    """Load and cache settings.yaml."""
    global _config
    if _config is None:
        config_path = os.path.join(os.path.dirname(__file__), "settings.yaml")
        with open(config_path) as f:
            _config = yaml.safe_load(f)
    return _config
