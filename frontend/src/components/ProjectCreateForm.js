import React from "react";

class ProjectCreateForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'name': '', 'link': '', 'users': null}
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.link, this.state.users)
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
        if (!event.target.selectedOptions){
            this.setState({
                'users': []
            })
            return;
        }
        let users = []
        for(let i = 0; i < event.target.selectedOptions.length; i++){
            users.push(event.target.selectedOptions.item(i).value)
        }

        this.setState({
                'users': users
            })
    }

    render() {
        return (
            <form className="project_form" onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" className="project_input" name="name" placeholder="Название проекта" value={this.state.name} onChange={(event) => this.handleChange(event)}/>
                <input type="url" className="project_input" name="link" placeholder="Ссылка на репозиторий" value={this.state.link} onChange={(event) => this.handleChange(event)}/>
                <select name="users" multiple onChange={(event) => this.handleChangeSelect(event)}>
                    <option selected="selected" disabled="disabled">Участники:</option>
                    {this.props.users.map((user) => <option name="users" value={user.id}>{user.username}</option>)}
                </select>
                <input type="submit" className="project_input_submit" value="Создать"/>
            </form>
        );
    }
}

export default ProjectCreateForm;