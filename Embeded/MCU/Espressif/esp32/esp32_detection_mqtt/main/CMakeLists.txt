idf_component_register(SRCS "main.c"
                      PRIV_REQUIRES spi_flash esp_wifi nvs_flash mqtt driver  ds18b20
                      INCLUDE_DIRS ".")