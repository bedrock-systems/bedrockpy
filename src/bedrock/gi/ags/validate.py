import pandas as pd


def check_ags_proj_group(proj_df: pd.DataFrame) -> bool:
    """Checks if the AGS 3 or AGS 4 PROJ group is correct.

    Args:
        proj_df (pd.DataFrame): The DataFrame with the PROJ group.

    Raises:
        ValueError: If AGS 3 of AGS 4 PROJ group is not correct.

    Returns:
        bool: Returns True if the AGS 3 or AGS 4 PROJ group is correct.
    """

    if len(proj_df) != 1:
        raise ValueError("The PROJ group must contain exactly one row.")

    project_id = proj_df["PROJ_ID"].iloc[0]
    if not project_id:
        raise ValueError(
            'The project ID ("PROJ_ID" in the "PROJ" group) is missing from the AGS data.'
        )

    return True
