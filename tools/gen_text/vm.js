class VMachine {
    constructor() {
        this.init()
    }

    static new(...args) {
        return new this(...args)
    }

    init() {
        this.setup()
        this.loadGuaAscii()
    }

    setup() {
        // 内存通电后全部置 0
        this.memory = Array(2 ** 10).fill(0)
        this.screen = GuaCanvas.new('#id-canvas')
        this.cpu = CPU.new()
        // 系统资源打包
        this.vars = {
            memory: this.memory,
            screen: this.screen,
        }
    }

    loadGuaAscii() {
        // 初始化加载编码表到内存
        let asciis = Object.values(ascii)
        log('gua_ascii', asciis)
        for (let i = 0; i < asciis.length; i++) {
            let asc = asciis[i]
            for (let j = 0; j < asc.length; j++) {
                let a = asc[j]
                let index = i * asc.length + j
                this.memory[index] = a
            }
        }
        log('memery', this.memory)


    }

    run(memory) {
        let cpu = this.cpu
        let funMap = this.registerFunMap
        for (let i = 0; i < memory.length;) {
            let offset = cpu.run(memory, i, this.vars)
            i += offset
        }

    }
}
