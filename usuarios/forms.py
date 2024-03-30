from django import forms

class LoginFroms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Gabriel Galani"
            }
        )
    )
    senha= forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

  
class CadastroFroms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Gabriel Galani"
            }
        )
    )
    
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: gabrielgalani@xpto.com"
            }
        )
    )
    
    senha_um= forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
    senha_dois= forms.CharField(
        label = "Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome=self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos no campo de nome de usuário")
            else:
                return nome

    
    def clean_senha_dois(self):
        senha_um=self.cleaned_data.get("senha_um")
        senha_dois=self.cleaned_data.get("senha_dois")
        
        if senha_um and senha_dois: 
            if senha_um != senha_dois: 
                raise forms.ValidationError("As senhas devem ser iguais!")
            else: 
                return senha_dois