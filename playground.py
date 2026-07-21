from gt100_builder import TSLParser

live = TSLParser("templates/LiveSet.tsl").load()

patch = live.patches[0]

print("Patch:", patch.name)
print("Gain:", patch.preamp.a.gain)
print("Delay:", patch.delay.time)
print("EQ:", patch.eq.low_gain)

patch.preamp.a.gain = 65

live.save("output/test.tsl")

print("Arquivo salvo!")