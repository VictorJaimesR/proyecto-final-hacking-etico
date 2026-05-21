from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()


class CouponApplyRequest(BaseModel):
    username: str
    coupon_code: str
    discount_percent: int


class CouponApplyResponse(BaseModel):
    username: str
    coupon_code: str
    applied_discount: int
    message: str


@router.post(
    "/coupons/apply",
    response_model=CouponApplyResponse,
    status_code=status.HTTP_200_OK,
)
async def apply_coupon(coupon: CouponApplyRequest):
    """
    Vulnerable endpoint created as project extension.

    Security issue:
    The API trusts the discount_percent value sent by the client.
    A normal user can submit an arbitrary discount value.
    """

    return CouponApplyResponse(
        username=coupon.username,
        coupon_code=coupon.coupon_code,
        applied_discount=coupon.discount_percent,
        message="Coupon applied without server-side validation",
    )

