from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

router = APIRouter()


class CouponApplyRequest(BaseModel):
    username: str
    coupon_code: str
    discount_percent: int  # Se ignorará este valor para la mitigación


class CouponApplyResponse(BaseModel):
    username: str
    coupon_code: str
    applied_discount: int
    message: str


# Diccionario de cupones válidos y su descuento real
VALID_COUPONS = {
    "ADMIN90": 10,      # solo 10% real
    "WELCOME10": 10,
    "SUMMER20": 20,
}


@router.post(
    "/coupons/apply",
    response_model=CouponApplyResponse,
    status_code=status.HTTP_200_OK,
)
async def apply_coupon(coupon: CouponApplyRequest):
    """
    Mitigated endpoint: server validates discount_percent based on coupon_code
    """

    # Verificar que el cupón exista
    if coupon.coupon_code not in VALID_COUPONS:
        raise HTTPException(status_code=400, detail="Coupon code invalid")

    # Usar solo el descuento seguro definido en el servidor
    applied_discount = VALID_COUPONS[coupon.coupon_code]

    return CouponApplyResponse(
        username=coupon.username,
        coupon_code=coupon.coupon_code,
        applied_discount=applied_discount,
        message="Coupon applied with server-side validation",
    )
