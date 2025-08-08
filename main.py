import streamlit as st
import streamlit_authenticator as stauth

COOKIE_EXPIRY_DAYS = 30

def main():
    # Criando o autenticador
    authenticator = stauth.Authenticate(
        {'username': {'teste': {'name': 'testando', 'password': 'test123'}}},
        'random_cookie_name',
        'random_signature_key',
        
        COOKIE_EXPIRY_DAYS, 
    )
    
    if 'click_register' not in st.session_state:
        st.session_state['click_register'] = False
        
    if st.session_state['click_register'] == False:
        login_form(authenticator=authenticator)
    
    
    
# Criando a tela de login
def login_form(authenticator):
    name, authentication_status, username = authenticator.login('Login')
    if authentication_status:
        authenticator.logout('Logout', main)
        st.title('Área do Dashboard')
        st.write(f'Bem vindo {name} !')
    elif authentication_status == False:
        st.error('Usuario/senha incorretos.')
    elif authentication_status == None:
        st.warning('Por favor, informe um usuário e senha')
        click_register = st.button("Registrar")
        if click_register:
            st.session_state['click_register'] = True
            st.rerun()


def confirm_msg():
    hashed_password = stauth.Hasher([st.session_state.pswd]).generate()
    if st.session_state.pswd != st.session_state.confirm_msg:
        st.warning('Senhas não conferem')
    elif 'consult_name()':
        st.warning('Nome de usuário já existe')
    else:
        'add_register()'
        st.success('Registro efetuado com sucesso !')

      
# Criando a tela de registro
def user_form():
    with st.form(key="formulario", clear_on_submit=True):
        nome = st.text_input('Nome', key="nome")
        username = st.text_input('Usuario', key='user')
        password = st.text_input("Senha", key="password", type="password")
        confirm_password = st.text_input("Confirme senha", key="confirm_pswd", type="confirm_pswd")
        submit = st.form_submit_button(
            "Salvar", on_click=confirm_msg
        )
        click_in_login = st.button("Fazer Login")
        
        if click_in_login:
            st.session_state['click_register'] = False
        
    if __name__ == '__main__':
        main()