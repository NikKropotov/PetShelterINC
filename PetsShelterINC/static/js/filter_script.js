function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

// const forms = document.querySelector('form[name=filter]');
//
// forms.addEventListener('submit', function (e) {
//     // Получаем данные из формы
//     e.preventDefault();
//     let url = this.action;
//     let params = new URLSearchParams(new FormData(this)).toString();
//     ajaxSend(url, params);
// });

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.container_cards_filters>.row>.main');
    div.innerHTML = output;
}

let html = '\
{{#pets}}\
    <a class="card-link" href="/{{ idpet }}">\
        <div class="card">\
            <div class="card__badges">\
                 <div class="card__badge card__badge--class">{{ pet_status }}</div>\
            </div>\
            <div class="card__img">\
                <img src="media/{{ petImagePath }}"\
                     alt="{{ pets_list.pet_name }}">\
            </div>\
             <div class="card__content">\
                  <h4 class="card__title">{{ pet_name }}</h4>\
             </div>\
        </div>\
    </a>\
{{/pets}}'