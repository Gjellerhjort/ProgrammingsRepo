idf_component_register(SRCS "main.c"
                      PRIV_REQUIRES spi_flash esp_wifi nvs_flash mqtt driver HD44780 
                      INCLUDE_DIRS ".")