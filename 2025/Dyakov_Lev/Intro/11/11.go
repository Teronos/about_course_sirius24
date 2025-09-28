package main

//Структуры:
//Роли
type role struct {
	Role_id   uint
	Role_name string
}

//Работники
type employee struct {
	Emp_id      uint
	First_name  string
	Second_name string
	grade       string
	roles       []role
	access_tags []string
	age         uint
	contacts    map[int]string
}

//Документы
type doc struct {
	Doc_id      uint
	Name        string
	Creator     *employee
	Changer     []*employee
	Location    string
	Tags        []string
	Description string
	access_role []*role
}

//Интерфейсы:

type doc_interface interface {
	create_doc() //создание документа
	change_doc() //изменение документа
	delete_doc() //удаление документа
}

type emp_interface interface {
	create_emp()      //создание сотрудника
	remove_emp()      //увольнение сотрудника
	change_roles()    //изменение ролей сотрудника
	change_contacts() //изменение контактов
	change_grade()    //изменение статуса
	add_tag_access()  //добавление дступных тегов
}

type role_interface interface {
	add_role()    //добавить новую роль
	delete_role() //удалить роль
}
