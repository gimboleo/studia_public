let points = document.getElementsByName('points')
let sum = document.getElementById('sum')
let submit = document.getElementById('submit')


function calculateSum() {
    let res = 0
    for (let p of points) res += +p.value || 0
    sum.value = res
}


points.forEach(e => {e.addEventListener("input", calculateSum)})
submit.onsubmit = () => {submit.setAttribute('readonly', '')}