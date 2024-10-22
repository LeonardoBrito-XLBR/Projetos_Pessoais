//DOM
const resumo = document.querySelector("#texto");
const imagem = document.querySelector("#capa");
const botao1 = document.querySelector("#filme1")
const botao2 = document.querySelector("#filme2")
const botao3 = document.querySelector("#filme3")
const botao4 = document.querySelector("#filme4")


//EVENTO
botao1.addEventListener("click", capa1)
botao2.addEventListener("click", capa2)  
botao3.addEventListener("click", capa3)
botao4.addEventListener("click", capa4)


// MUDAR O RESUMO DE CADA CAPA DE FILME
function capa1(){
    imagem.src='image/imagem6.jpg'
    resumo.textContent = 'Com o retorno do Imperador Palpatine, a Resistência toma a frente da batalha. Treinando para ser uma completa Jedi, Rey se encontra em conflito com passado e futuro, e teme pelas respostas que pode conseguir com Kylo Ren.'
}

function capa2(){
    imagem.src="image/image2.jpg"
    resumo.textContent="A queda de Darth Vader e do Império levou ao surgimento de uma nova força sombria: a Primeira Ordem. Eles procuram o jedi Luke Skywalker, desaparecido. A resistência tenta desesperadamente encontrá-lo antes para salvar a galáxia."
}

function capa3(){
    imagem.src="image/image1.png"
    resumo.textContent="A história da franquia é ambientada em uma galáxia distante, onde a luta entre o bem e o mal é o cerne da narrativa. A Aliança Rebelde é formada por um grupo de planetas que se unem para lutar contra o Império Galáctico, liderado pelo temido Darth Vader e pelo Imperador Palpatine."
}

function capa4(){
    imagem.src="image/image09.webp"
    resumo.textContent='A tranquila e solitária vida de Luke Skywalker sofre uma reviravolta quando ele conhece Rey, uma jovem que mostra fortes sinais da Força. O desejo dela de aprender o estilo dos Jedi força Luke a tomar uma decisão que mudará sua vida para sempre. Enquanto isso, Kylo Ren e o General Hux lideram a Primeira Ordem para um ataque total contra Leia e a Resistência pela supremacia da galáxia.' 
}  