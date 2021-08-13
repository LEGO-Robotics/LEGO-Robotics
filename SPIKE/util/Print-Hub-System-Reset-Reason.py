from pybricks.hubs import InventorHub


hub = InventorHub()

print(f'Hub System Reset Reason: {hub.system.reset_reason()}')
