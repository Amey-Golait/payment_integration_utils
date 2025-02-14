import click
from payment_integration_utils_mode_co.constants import BUG_REPORT_URL
from payment_integration_utils_mode_co.hooks import app_title as APP_NAME
from payment_integration_utils_mode_co.setup import delete_customizations


def before_uninstall():
    try:
        delete_customizations()
    except Exception as e:
        click.secho(
            (
                f"\nUninstallation of {APP_NAME} failed due to an error."
                "Please try re-uninstalling the app or "
                f"report the issue on {BUG_REPORT_URL} if not resolved."
            ),
            fg="bright_red",
        )
        raise e

    click.secho(f"Thank you for using {APP_NAME}!", fg="green")
