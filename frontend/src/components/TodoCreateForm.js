import React from "react";

class TodoCreateForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'text': '', 'creator': null, 'project': null}
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.text, this.state.creator, this.state.project)
        event.preventDefault()
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleChangeSelect(event) {
        this.setState(
            {
                [event.target.selectedOptions.item(0).attributes.name.value]: event.target.selectedOptions.item(0).value
            }
        )
    }

    render() {
        return (
            <form className="todo_create_form" onSubmit={(event) => this.handleSubmit(event)}>
                <textarea className="todo_create_textarea" name="text" placeholder="Текст заметки" value={this.state.text} onChange={(event) => this.handleChange(event)}/>
                <select name="creator" onChange={(event) => this.handleChangeSelect(event)}>
                    <option selected="selected" disabled="disabled">Создатель:</option>
                    {this.props.users.map((user) => <option name="creator" value={user.id}>{user.username}</option>)}
                </select>
                <select name="project" onChange={(event) => this.handleChangeSelect(event)}>
                    <option selected="selected" disabled="disabled">Проект:</option>
                    {this.props.projects.map((project) => <option name="project" value={project.id}>{project.name}</option>)}
                </select>
                <input type="submit" className="todo_create_input_submit" value="Создать"/>
            </form>
        );
    }
}

export default TodoCreateForm;