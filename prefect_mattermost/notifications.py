from typing import Optional
from pydantic import Field, SecretStr

from prefect.blocks.notifications import NotificationBlock
from prefect.utilities.asyncutils import sync_compatible

class MattermostWebhook(NotificationBlock):
    """
    Enables sending notifications via a provided Mattermost webhook.
    Args:
        url (SecretStr): Mattermost webhook URL which can be used to send messages
    Examples:
        Load a saved Mattermost webhook and send a message:
        ```python
        from my_notifications import MattermostWebhook
        mattermost_webhook_block = MattermostWebhook.load("BLOCK_NAME")
        mattermost_webhook_block.notify("Hello from Prefect!")
        ```
    """

    _block_type_name = "Mattermost Webhook"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/7dkzINU9r6j44giEFuHuUC/85d4cd321ad60c1b1e898bc3fbd28580/5cb480cd5f1b6d3fbadece79.png?h=250"

    url: SecretStr = Field(
        ...,
        title="Webhook URL",
        description="Mattermost's incoming webhook URL used to send notifications.",
        example="https://your-hook.cloud.mattermost.com/hooks/XXX",
    )

    def block_initialization(self) -> None:
        from httpx import AsyncClient
        self._async_webhook_client = AsyncClient()

    @sync_compatible
    async def notify(self, body: str, subject: Optional[str] = None):
        print(self.url.get_secret_value())
        await self._async_webhook_client.post(url=self.url.get_secret_value(), json={"text": body})