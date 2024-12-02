const formPesquisa = document.querySelector("form");
const pages = document.querySelector(".pages")
const totalPages = document.querySelector(".total-pages")
const atualPages = document.querySelector(".current-page")
const btnSearch = document.querySelector("#botao")

const apikey = '346c304d';

let page = 1;

const searchMovies = (page) => {
    console.log(page)
    
    const pesquisa = document.getElementById("pesquisa").value
    // const pesquisa = ev.target.pesquisa.value;

    
    if (pesquisa === ""){
        alert("Preencha o campo!")
        return;
    }

    fetch(`https://www.omdbapi.com/?s=${pesquisa}&apikey=${apikey}&page=${page}`)
        .then(result => result.json())
        .then(json => carregaLista(json));
}


const carregaLista = (json) => {
    const lista = document.querySelector(".lista")
    lista.innerHTML = "";

    const totalResults = Number(json.totalResults)
    totalPages.textContent = `${Math.round(totalResults /10)}`



    if (json.Response == 'False'){
        alert('Nenhum filme encontrado');
        return
    }

    json.Search.forEach(element => {

        let item = document.createElement("div")
        item.classList.add("item");

        // PROCURAR UMA FORMA DE ATRIBUIR OS VALORES DO JSON
        item.innerHTML = `<img src="${element.Poster}" /><h2>${element.Title}</h2>`;

        lista.appendChild(item);
    });

    pages.classList.add("active") //MESMA LOGICA DO DARK E LIGHT
}

const changesPages = (e) => {
    const buttonClicked = e.srcElement;
    console.log(buttonClicked)
    

    if (buttonClicked.classList.contains('last-page')){
        if (page<=1) return;

        page -=1;
        atualPages.textContent = page
        searchMovies(page)
        console.log("Esquerda")
    }
    
    if (buttonClicked.classList.contains('next-page')){
        if(page>=totalPages.textContent) return;
        
        page +=1;
        atualPages.textContent = page
        searchMovies(page)
        console.log("Direita")
    }
}


pages.addEventListener("click", changesPages);
btnSearch.addEventListener("click", searchMovies);

formPesquisa.addEventListener('submit', (e) => e.preventDefault()) 

document.getElementById("pesquisa").addEventListener('change', () =>{
    page=1
    atualPages.textContent = page;
} )


