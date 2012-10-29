from builder.models import Variable

def writeTemplates(Form):
    newTemplate = open("../newdanger/stroke/templates/CT.html", "w+")
    templateWriter = open("../newdanger/stroke/templates/CT.html", "a")
    Order = eval(Form.VariableOrder)
    for Each in Order:
        Var = Variable.objects.get(id=Each)
        if Var.FieldType == "RadioButton":
            templateWriter.write("""<!--  %s  -->
<div class="control-group{%% if form.%s.errors %%} error{%% endif %%}">
    <div class="controls" id="divid_{{ form.%s.name }}">
                    
            <span><h5>{{ form.%s.label }}&nbsp;</h5></span><br>
                    
            {%% for option in form.%s %%}
            {{ option.tag }} {{ option.choice_label }}<br>
            {%% endfor %%}
                   
            {%% for error in form.%s.errors %%}
                <span class="help-inline">{{ error }}</span>
            {%% endfor %%}

            {%% if form.%s.help_text %%}
            <p class="help-block">
                {{ form.%s.help_text }}
            </p>
        {%% endif %%}
    </div>
</div>\n\n""" % (Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName))
        elif Var.FieldType == "BooleanField":
            templateWriter.write("""<!--  %s  -->
<div class="control-group{%% if form.%s.errors %%} error{%% endif %%}">
        <div class="controls" id="divid_{{ form.%s.name }}">
                    <label class="checkbox">
                        {{ form.%s }} <span>{{ form.%s.label }}&nbsp;</span>
                    </label>

                    {%% for error in form.%s.errors %%}
                        <span class="help-inline">{{ error }}</span>
                    {%% endfor %%}

                    {%% if form.%s.help_text %%}
                    <p class="help-block">
                        {{ form.%s.help_text }}
                    </p>
                    {%% endif %%}
                </div>
</div>\n\n""" % (Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName))
        else:
            templateWriter.write("""<!--  %s  -->
<div class="control-group{%% if form.%s.errors %%} error{%% endif %%}">
        <div class="controls" id="divid_{{ form.%s.name }}">
        <div class="control-label"><h5>{{ form.%s.label }}&nbsp;</h5></div>

        <div class="controls">
            {{ form.%s }}

            {%% for error in form.%s.errors %%}
                <span class="help-inline">{{ error }}</span>
            {%% endfor %%}

            {%% if form.%s.help_text %%}
            <p class="help-block">
                {{ form.%s.help_text }}
            </p>
            {%% endif %%}

        </div>
</div>\n\n""" % (Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName, Var.VarName))

