from pybricks.hubs import InventorHub


hub = InventorHub()

print('Hub System Reset Reason:', hub.system.reset_reason())
