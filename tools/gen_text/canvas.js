class GuaCanvas extends GuaObject{
    constructor(selector) {
        super()
        this.setup(selector)

    }

    setup(selector) {
        let canvas = _e(selector)
        this.canvas = canvas
        this.context = canvas.getContext('2d')
        this.w = canvas.width
        this.h = canvas.height
        this.size = this.w * this.h
        this.pixels = this.context.getImageData(0, 0, this.w, this.h)
        this.bytesPerPixel = 4
        // element
        this.elements = []
        this.white = 0b1111111111111111
        this.black = 0b1111000000000000
    }

    render() {
        // 执行这个函数后, 才会实际地把图像画出来
        // ES6 新语法, 取出想要的属性并赋值给变量, 不懂自己搜「ES6 新语法」
        let {pixels, context} = this
        context.putImageData(pixels, 0, 0)
    }

    rgbaFromColor(color) {
        let r = ((color >> 0) & 0x0f) * 255 / 0x0f
        let g = ((color >> 4) & 0x0f) * 255 / 0x0f
        let b = ((color >> 8) & 0x0f) * 255 / 0x0f
        let a = ((color >> 12) & 0x0f) * 255 / 0x0f
        return [r, g, b, a]
    }

    draw(color, i) {
        let {context, pixels} = this
        let data = pixels.data
        //   let [r, g, b , a] = data.slice(i, i + 4)
        let [r, g, b, a] = this.rgbaFromColor(color)

        // log('rgba', color, r, g, b, a)
        data[i] = r
        data[i+1] = g
        data[i+2] = b
        data[i+3] = a
        this.render()
    }

    drawPoint(point, index) {
        let i = index
        let {context, pixels} = this
        let data = pixels.data
        //   let [r, g, b , a] = data.slice(i, i + 4)
        let color = point === 0 ? this.white : this.black
        let [r, g, b, a] = this.rgbaFromColor(color)

        data[i] = r
        data[i+1] = g
        data[i+2] = b
        data[i+3] = a
        this.render()
    }

    _drawTextLine(text, index) {
        // 画线
        let i = index
        for (let j = 0; j < 8; j++) {
            let p = (text >> j) & 0x01
            this.drawPoint(p, i)
            i += 32 * 4
        }
    }

    drawText(txt, index) {
        // ascii 字体, [254, 130, 254, 0]
        let i = index
        let {context, pixels} = this
        let data = pixels.data
        //   let [r, g, b , a] = data.slice(i, i + 4)
        for (let j = 0; j < txt.length; j++) {
            let t = txt[j]
            this._drawTextLine(t, i)
            i += 4
        }
    }

    __debug_draw_demo() {
        // 这是一个 demo 函数, 用来给你看看如何设置像素
        // ES6 新语法, 取出想要的属性并赋值给变量, 不懂自己搜「ES6 新语法」
        let {context, pixels} = this
        // 获取像素数据，data 是一个数组
        let data = pixels.data
        // 一个像素 4 字节，分别表示 r g b a
        for (let i = 0; i < data.length; i += 4) {
            let [r, g, b , a] = data.slice(i, i + 4)
            r = 255
            a = 255
            data[i] = r
            data[i+3] = a
        }
        context.putImageData(pixels, 0 , 0)
    }
}
