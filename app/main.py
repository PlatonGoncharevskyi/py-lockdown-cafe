from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    all_normal = True
    masks_to_buy = 0
    for el in friends:
        if not el["wearing_a_mask"]:
            masks_to_buy += 1
        try:
            cafe.visit_cafe(el)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    if all_normal:
        return f"Friends can go to {cafe.name}"
