idf_component_register(
    SRCS "ds18b20.c"
    INCLUDE_DIRS "include"
    PRIV_REQUIRES driver esp_timer
    REQUIRES owb

)