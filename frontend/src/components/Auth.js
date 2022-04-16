import React from "react";

class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'login': '', 'password': ''}
    }

    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password)
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
            <form className="login_form" onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" className="login_input" name="login" placeholder="Логин" value={this.state.login} onChange={(event) => this.handleChange(event)}/>
                <input type="password" className="login_input" name="password" placeholder="Пароль" value={this.state.password} onChange={(event) => this.handleChange(event)}/>
                <input type="submit" className="login_input_submit" value="Войти"/>
                <input type="submit" className="login_input_submit" value="Зарегистрироваться"/>
            </form>
        );
    }
}

export default LoginForm;