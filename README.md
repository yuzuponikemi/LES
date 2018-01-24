# LES
for LES data processing




#メモ
x = np.linspace(0, 2*pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)  #新たにcosを計算

pyplot.plot(x, sin_y, label='sin')
pyplot.plot(x, cos_y, label='cos')  #cosの値をプロット

#グラフタイトル
pyplot.title('Sin And Cos Graph')

#グラフの軸
pyplot.xlabel('X-Axis')
pyplot.ylabel('Y-Axis')

#グラフの凡例
pyplot.legend()

pyplot.show()
