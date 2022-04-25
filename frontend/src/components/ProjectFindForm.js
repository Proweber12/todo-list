import React from "react";

class ProjectFindForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'search': ''}
    }

    handleSubmit(event) {
        this.props.findProject(this.state.search)
        history.back()
        event.preventDefault()
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    render() {
        return (
            <form className="project_form" onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" className="project_input" name="search" placeholder="Название проекта" value={this.state.search} onChange={(event) => this.handleChange(event)}/>
                <input type="submit" className="project_input_submit" value="Найти"/>
            </form>
        );
    }
}

export default ProjectFindForm;