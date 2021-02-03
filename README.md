# Django Rest Framework: Blog

Приложение реализует API для создания и просмотра постов в блоге и их категорий.  
Приложение развёрнуто на [Heroku](https://safe-cliffs-55556.herokuapp.com/).

## Получить список всех постов
```
GET https://safe-cliffs-55556.herokuapp.com/
```
  
Пример запроса и ответа в httpie:
```
https https://safe-cliffs-55556.herokuapp.com/
  
HTTP/1.1 200 OK
[
    {
        "author": null,
        "category": "Приключения",
        "content": "Ходили гулять",
        "id": 3,
        "publication_date": "2021-02-03T14:59:23.659959Z",
        "slug": "walking-day",
        "status": "D",
        "title": "Прогулка с друзьями",
        "updated": "2021-02-03T14:59:23.659940Z"
    }
]
```

## Создать новый пост
```
POST https://safe-cliffs-55556.herokuapp.com/
```
Пример данных поста в запросе:
```
{"title": "Прогулка с друзьями", "category": "Приключения", "slug": "walking-day", "status": "P", "content": "Ходили гулять"}
```
Поля **title**, **slug**, **status**, **content** являются обязательными.  
В поле **category** необходимо указать существующую категорию (как получить список категорий, см. ниже).  
  
В ответ на успешное создание возвращается ответ **201** и созданный пост с присвоенным **id** и полями **publication_date** и **updated**.
  
Пример запроса и ответа в httpie:
```
https POST https://safe-cliffs-55556.herokuapp.com/ title='Прогулка с друзьями' slug=walking-day status=D content='Ходили гулять' category='Приключения'
  
HTTP/1.1 201 Created
{
    "author": null,
    "category": "Приключения",
    "content": "Ходили гулять",
    "id": 3,
    "publication_date": "2021-02-03T14:59:23.659959Z",
    "slug": "walking-day",
    "status": "D",
    "title": "Прогулка с друзьями",
    "updated": "2021-02-03T14:59:23.659940Z"
}
```
  
## Получить данные по конкретному посту
```
GET https://safe-cliffs-55556.herokuapp.com/categories/<id>
```
  
Пример запроса и ответа в httpie:
```
https https://safe-cliffs-55556.herokuapp.com/3
  
HTTP/1.1 200 OK
{
    "author": null,
    "category": "Приключения",
    "content": "Ходили гулять",
    "id": 3,
    "publication_date": "2021-02-03T14:59:23.659959Z",
    "slug": "walking-day",
    "status": "D",
    "title": "Прогулка с друзьями",
    "updated": "2021-02-03T14:59:23.659940Z"
}
```
  
## Получить список всех категорий

```
GET https://safe-cliffs-55556.herokuapp.com/categories
```
В поле **posts** отображается список постов, которым назначена эта категория.
  
Пример запроса и ответа в httpie:
```
https https://safe-cliffs-55556.herokuapp.com/categories
  
HTTP/1.1 200 OK
[
    {
        "id": 2,
        "posts": [
            {
                "author": null,
                "category": "Приключения",
                "content": "Ходили гулять",
                "id": 3,
                "publication_date": "2021-02-03T14:59:23.659959Z",
                "slug": "walking-day",
                "status": "D",
                "title": "Прогулка с друзьями",
                "updated": "2021-02-03T14:59:23.659940Z"
            }
        ],
        "title": "Приключения"
    }
]
```

## Создать новую категорию
```
POST https://safe-cliffs-55556.herokuapp.com/categories
```
Пример данных категории в запросе:
```
{"title": "Приключения"}
```
Поле **title** является обязательным.  
В ответ на успешное создание возвращается **201** и созданная категория с присвоенным **id**.  
  
Пример запроса и ответа в httpie:
```
https POST https://safe-cliffs-55556.herokuapp.com/categories title=Приключения
  
HTTP/1.1 201 Created
{
    "id": 2,
    "posts": [],
    "title": "Приключения"
}
```

## Получить данные по конкретной категории
```
GET https://safe-cliffs-55556.herokuapp.com/categories/<id>
```
Пример запроса и ответа в httpie:
```
https https://safe-cliffs-55556.herokuapp.com/categories/2
  
HTTP/1.1 200 OK
{
    "id": 2,
    "posts": [
        {
            "author": null,
            "category": "Приключения",
            "content": "Ходили гулять",
            "id": 3,
            "publication_date": "2021-02-03T14:59:23.659959Z",
            "slug": "walking-day",
            "status": "D",
            "title": "Прогулка с друзьями",
            "updated": "2021-02-03T14:59:23.659940Z"
        }
    ],
    "title": "Приключения"
}
```
