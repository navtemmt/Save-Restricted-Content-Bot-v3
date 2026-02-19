# Copyright (c) 2025 devgagan : https://github.com/devgaganin
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import asyncio
from shared_client import start_client
import importlib
import os
import sys

print(">>> A: entered main.py")  # debug

async def load_and_run_plugins():
    print(">>> B: in load_and_run_plugins, starting start_client()")  # debug
    await start_client()
    print(">>> C: start_client() finished, loading plugins")  # debug

    plugin_dir = "plugins"
    plugins = [
        f[:-3]
        for f in os.listdir(plugin_dir)
        if f.endswith(".py") and f != "__init__.py"
    ]

    print(f">>> D: plugins found: {plugins}")  # debug

    for plugin in plugins:
        print(f">>> E: importing plugin {plugin}")  # debug
        module = importlib.import_module(f"plugins.{plugin}")
        if hasattr(module, f"run_{plugin}_plugin"):
            print(f"Running {plugin} plugin...")
            await getattr(module, f"run_{plugin}_plugin")()
        else:
            print(f">>> F: plugin {plugin} has no run_{plugin}_plugin, skipping")  # debug

async def main():
    print(">>> G: entering main()")  # debug
    await load_and_run_plugins()
    print(">>> H: plugins initialized, entering idle loop")  # debug
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    # Modern, warning-free event loop initialization
    try:
        loop = asyncio.get_running_loop()
        print(">>> I: reusing existing running event loop")  # debug
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print(">>> I: created and set new event loop")  # debug

    print("Starting clients ...")
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(">>> ERROR in main:", e)
        sys.exit(1)
    finally:
        try:
            if not loop.is_closed():
                loop.close()
        except Exception:
            pass
