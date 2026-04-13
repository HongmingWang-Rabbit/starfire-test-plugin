"""Claude Code adaptor for starfire-test-plugin.

Delegates to the built-in AgentskillsAdaptor, which handles the standard
rules + skills plugin shape. This file exists to prove that an external
github:// plugin can ship its own runtime adaptor end-to-end.
"""
from plugins_registry.builtins import AgentskillsAdaptor as Adaptor

__all__ = ["Adaptor"]
