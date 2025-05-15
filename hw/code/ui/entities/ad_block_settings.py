import enum
from typing import Literal, Optional, TypedDict
from ui.components.cpm_setting import CPMSpecification
from ui.components.ad_block_design_settings import BlockDesignSettings

BlockFormat = Literal["display_block"] | Literal["recommend_widget"] | Literal['amp_display_block']
IntegrationType = Optional[Literal['direct'] | Literal['header_bidding']]
ShowPeriod = Literal['day'] | Literal['week'] | Literal['month']

class AdBlockSettings(TypedDict):
    is_amp: bool
    name: str
    format: BlockFormat
    size: Optional[str]
    design: Optional[BlockDesignSettings]
    integration_type: IntegrationType
    cpm: Optional[CPMSpecification]
    call_code: Optional[str]
    show_limit: int
    period: ShowPeriod
    interval: int

class AdBlockStatus(enum.IntEnum):
    ARCHIVED = 1
    STOPPED = 2
