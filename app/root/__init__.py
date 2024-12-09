from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .location_route import location_bp
    from .heartratealerts_route import heartratealerts_bp
    from .alertscontacts_route import alertscontacts_bp
    from .batterystatus_route import batterystatus_bp
    from .locationalerts_route import locationalerts_bp
    from .smartwathes_route import smartwatches_bp
    from .owners_route import owners_bp
    from .batteryalerts_route import batteryalerts_bp
    from .notificationsettings_route import notificationsettings_bp
    from .heartrates_route import heartrates_bp

    app.register_blueprint(heartratealerts_bp)
    app.register_blueprint(alertscontacts_bp)
    app.register_blueprint(batterystatus_bp)
    app.register_blueprint(locationalerts_bp)
    app.register_blueprint(smartwatches_bp)
    app.register_blueprint(owners_bp)
    app.register_blueprint(batteryalerts_bp)
    app.register_blueprint(notificationsettings_bp)
    app.register_blueprint(heartrates_bp)
    app.register_blueprint(location_bp)

