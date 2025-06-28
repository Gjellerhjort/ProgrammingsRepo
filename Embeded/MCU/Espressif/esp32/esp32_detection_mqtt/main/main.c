#include <stdio.h>
#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "nvs_flash.h"
#include "mqtt_client.h"
#include "esp_log.h"
#include "secrets.h"

#define MQTT_BROKER    "mqtt://192.168.1.48 // e.g. "mqtt://192.168.1.100"
#define MQTT_TOPIC     "esp32/test"

static const char *TAG = "MQTT_EXAMPLE";

static void wifi_init(void)
{
    esp_netif_init();
    esp_event_loop_create_default();
    esp_netif_create_default_wifi_sta();

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&cfg);

    wifi_config_t wifi_config = {};
    strcpy((char *)wifi_config.sta.ssid, WIFI_SSID);
    strcpy((char *)wifi_config.sta.password, WIFI_PASS);

    esp_wifi_set_mode(WIFI_MODE_STA);
    esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_config);
    esp_wifi_start();
    esp_wifi_connect();
}

static void mqtt_publish_task(void *arg)
{
    esp_mqtt_client_handle_t client = (esp_mqtt_client_handle_t)arg;
    int msg_id = 0;
    while (1) {
        char msg[64];
        snprintf(msg, sizeof(msg), "Hello from ESP32C3! Count: %d", msg_id++);
        esp_mqtt_client_publish(client, MQTT_TOPIC, msg, 0, 1, 0);
        ESP_LOGI(TAG, "Published: %s", msg);
        vTaskDelay(pdMS_TO_TICKS(60000)); // 1 minute
    }
}

static esp_err_t mqtt_event_handler_cb(esp_mqtt_event_handle_t event)
{
    esp_mqtt_client_handle_t client = event->client;
    switch (event->event_id) {
        case MQTT_EVENT_CONNECTED:
            ESP_LOGI(TAG, "MQTT_EVENT_CONNECTED");
            xTaskCreate(mqtt_publish_task, "mqtt_publish_task", 4096, client, 5, NULL);
            break;
        default:
            break;
    }
    return ESP_OK;
}

void app_main(void)
{
    nvs_flash_init();
    wifi_init();

    esp_mqtt_client_config_t mqtt_cfg = {
        .uri = MQTT_BROKER,
        .username = MQTT_USER,
        .password = MQTT_PASS,
    };
    esp_mqtt_client_handle_t client = esp_mqtt_client_init(&mqtt_cfg);
    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, mqtt_event_handler_cb, NULL);
    esp_mqtt_client_start(client);
}