import pandera as pa
from pandera.typing import Series


class Ags3HOLE(pa.DataFrameModel):
    HOLE_ID: Series[str] = pa.Field(
        # primary_key=True,
        unique=True,
        coerce=True,
        description="Exploratory hole or location equivalent",
        # example="327/16A",
    )
    HOLE_TYPE: Series[str] = pa.Field(
        coerce=True,
        # isin=["CP", "TP", "TPS", "TPS2", "TPS3", "TPS4", "TPS5", "TPS6", "TPS7", "TPS8"],
        description="Type of exploratory hole",
        # example="CP (See Appendix 1)",
    )
    HOLE_NATE: Series[float] = pa.Field(coerce=True)
    HOLE_NATN: Series[float] = pa.Field(coerce=True)
    HOLE_GL: Series[float] = pa.Field(coerce=True)
    HOLE_FDEP: Series[float] = pa.Field(
        coerce=True,
        description="Final depth of hole",
        # example=32.60,
        metadata={"unit": "m"},
    )


class BaseSAMP(pa.DataFrameModel):
    SAMP_TOP: Series[float] = pa.Field(
        coerce=True,
        description="Depth to TOP of sample",
        # example=24.55,
        metadata={"unit": "m"},
    )
    SAMP_BASE: Series[float] = pa.Field(
        coerce=True,
        nullable=True,
        description="Depth to BASE of sample",
        # example=24.55,
        metadata={"unit": "m"},
    )
    SAMP_TYPE: Series[str] = pa.Field(
        coerce=True,
        nullable=True,
        description="Sample type",
        # example="U (See Appendix 1)",
    )


class Ags3SAMP(BaseSAMP):
    SAMP_REF: Series[str] = pa.Field(
        # primary_key=True,
        unique=True,
        coerce=True,
        description="Sample reference number",
        # example="24",
    )
    HOLE_ID: Series[str] = pa.Field(
        # foreign_key="Ags3HOLE.HOLE_ID",
        coerce=True,
        description="Exploratory hole or location equivalent",
        # example="327/16A",
    )


class Ags4SAMP(BaseSAMP):
    SAMP_ID: Series[str] = pa.Field(
        # primary_key=True,
        unique=True,
        coerce=True,
        description="Sample unique identifier",
        # example="ABC121415010",
    )
    LOCA_ID: Series[str] = pa.Field(
        # foreign_key="Ags4LOCA.LOCA_ID",
        coerce=True,
        description="Location identifier",
        # example="327/16A",
    )
    SAMP_REF: Series[str] = pa.Field(
        coerce=True,
        description="Sample reference",
        # example="24",
    )


class BaseGEOL(pa.DataFrameModel):
    GEOL_TOP: Series[float] = pa.Field(
        coerce=True,
        description="Depth to the top of stratum",
        # example=16.21,
        metadata={"unit": "m"},
    )
    GEOL_BASE: Series[float] = pa.Field(
        coerce=True,
        description="Depth to the base of description",
        # example=17.25,
        metadata={"unit": "m"},
    )
    GEOL_DESC: Series[str] = pa.Field(
        coerce=True,
        description="General description of stratum",
        # example="Stiff grey silty CLAY",
    )
    GEOL_LEG: Series[str] = pa.Field(
        coerce=True,
        nullable=True,
        description="Legend code",
        # example="102",
    )
    GEOL_GEOL: Series[str] = pa.Field(
        coerce=True,
        description="Geology code",
        # example="LC",
    )
    GEOL_GEO2: Series[str] = pa.Field(
        coerce=True,
        nullable=True,
        description="Second geology code",
        # example="SAND",
    )


class Ags3GEOL(BaseGEOL):
    HOLE_ID: Series[str] = pa.Field(
        # foreign_key="Ags3HOLE.HOLE_ID",
        coerce=True,
        description="Exploratory hole or location equivalent",
        # example="6421/A",
    )


class Ags4GEOL(BaseGEOL):
    LOCA_ID: Series[str] = pa.Field(
        # foreign_key="Ags4LOCA.LOCA_ID",
        coerce=True,
        description="Location identifier",
        # example="327/16A",
    )