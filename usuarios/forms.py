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