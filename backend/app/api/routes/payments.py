from fastapi import APIRouter

router = APIRouter(prefix="/payments", tags=["payments"])

# TODO: Implement payment routes
# POST /checkout
# POST /listing-checkout
# POST /webhook
# GET /history
# POST /refund/{booking_id}
