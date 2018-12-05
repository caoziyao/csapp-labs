const log = console.log.bind(console)

const _e = (sel) => document.querySelector(sel)

const _es = (sel) => document.querySelectorAll(sel)

const bindAll = (sel, callback) => {
    let es = document.querySelectorAll(sel)
    for (let i = 0; i < es.length; i++) {
        let e = es[i]
        e.addEventListener('click', callback)
    }
}

const replacePos = (strObj, pos, replacetext) => {
    let str = strObj.substr(0, pos) + replacetext + strObj.substring(pos + 1, strObj.length);
    return str;
}
