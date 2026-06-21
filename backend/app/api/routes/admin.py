from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

# TODO: Implement admin routes
# GET /analytics
# GET /verifications
# PATCH /verifications/{id}/approve
# PATCH /verifications/{id}/reject
# POST /verifications/{id}/request-docs
# GET /users
# PATCH /users/{id}/suspend
# GET /disputes
# PATCH /disputes/{id}/resolve
# GET /reviews
# DELETE /reviews/{id}
