import os


def import_all(controller_dir, app):
    for filename in os.listdir(controller_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            # Construct the module name by removing the extension
            module_name = filename[:-3]
            # Import the module
            module = __import__(f"controller.{module_name}", fromlist=[module_name])
            # Get the blueprint from the imported module (assuming it's named the same as the file)
            blueprint = getattr(module, module_name)
            # Register the blueprint with the app
            app.register_blueprint(blueprint)
