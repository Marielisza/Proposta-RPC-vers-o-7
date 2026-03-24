# --- GERAÇÃO DO PDF ---
        pdf = FPDF()
        
        # ==========================================
        # PÁGINA 1: CAPA (Fundo Vermelho)
        # ==========================================
        pdf.add_page()
        
        # Fundo Vermelho Escuro (Padrão Dr. Fiscal)
        pdf.set_fill_color(200, 20, 30) # Ajuste o RGB conforme o tom exato da marca
        pdf.rect(0, 0, 210, 297, 'F')
        
        # Tenta inserir a logo na capa se ela existir (ajuste o nome do arquivo se necessário)
        if os.path.exists('logo_branca.png'):
            pdf.image('logo_branca.png', 85, 20, w=40)
        
        pdf.set_text_color(255, 255, 255) # Texto Branco
        
        # Bloco: EMPRESA
        pdf.set_y(100)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 6, "EMPRESA", ln=True, align='L')
        pdf.set_font("Arial", '', 20)
        pdf.multi_cell(0, 10, razao_social.upper(), align='L')
        
        pdf.ln(15)
        
        # Bloco: SERVIÇO
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 6, "SERVICO", ln=True, align='L')
        pdf.set_font("Arial", '', 18)
        pdf.multi_cell(0, 8, "Retificacoes Das Declaracoes\ne Compensacoes Mensais", align='L')
        
        pdf.ln(15)
        
        # Bloco: EMISSÃO
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 6, "EMISSAO", ln=True, align='L')
        pdf.set_font("Arial", '', 16)
        data_emissao = datetime.today().strftime('%d/%m/%Y')
        pdf.cell(0, 8, data_emissao, ln=True, align='L')

        # ==========================================
        # PÁGINA 2: CONTEÚDO TÉCNICO E VALORES
        # ==========================================
        pdf.add_page()
        pdf.set_text_color(0, 0, 0) # Volta para o texto preto
        
        # Tenta inserir a logo colorida no cabeçalho
        if os.path.exists('logo_colorida.png'):
            pdf.image('logo_colorida.png', 10, 10, w=30)
            pdf.ln(20)
        else:
            pdf.set_y(20) # Espaçamento caso não tenha logo

        # 1. Contexto
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Contexto", ln=True)
        pdf.set_font("Arial", '', 11)
        texto_contexto = (
            f"A {razao_social} apos a identificacao das oportunidades apresentadas no trabalho de "
            "Diagnostico Tributario apresentado pela Dr. Fiscal, verificou que a habilitacao dos "
            "creditos de PIS e COFINS, dependem da retificacao das informacoes constantes da DCTF "
            "e EFD Contribuicoes."
        )
        pdf.multi_cell(0, 6, texto_contexto)
        pdf.ln(5)

        # 2. Objetivo
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Objetivo", ln=True)
        pdf.set_font("Arial", '', 11)
        texto_objetivo = (
            "O servico de Retificacoes e Procedimentos de Compensacao preve a retificacao de todas "
            "as obrigacoes fiscais acessorias necessarias para a correta habilitacao dos ativos "
            "identificados no trabalho de Diagnostico Tributario. Estao contempladas no escopo "
            "dessa proposta a retificacao de DCTF, EFD Contribuicoes, bem como a preparacao dos "
            "pedidos de ressarcimentos, compensacoes mensais e alem de todas as diligencias.\n\n"
            "O grande diferencial dos servicos prestados pela Dr. Fiscal atraves deste escopo e a "
            "profundidade dos exames e analises, assim como o emprego de horas tecnicas de "
            "especialistas em Declaracoes Eletronicas."
        )
        pdf.multi_cell(0, 6, texto_objetivo)
        pdf.ln(5)

        # 3. Escopo
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Escopo", ln=True)
        pdf.set_font("Arial", '', 11)
        texto_escopo = (
            "A Dr. Fiscal prestara servicos de consultoria fiscal, no sentido de retificacao das "
            "obrigacoes fiscais acessorias, de acordo com as orientacoes e regulamentacoes emitidas "
            "pela Receita Federal do Brasil, com o objetivo de habilitar eventuais ativos que a "
            "empresa tenha direito de receber."
        )
        pdf.multi_cell(0, 6, texto_escopo)
        pdf.ln(5)

        # 4. Investimento
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Investimento", ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 6, "A seguir, descrevemos o investimento proposto para cada escopo dos trabalhos apresentados:")
        
        # Tópicos do Investimento
        pdf.ln(2)
        pdf.multi_cell(0, 6, f"a) Remuneracao: R$ {formatar_real(total_servico)} condicionado a avaliacao da proposta dentro da validade prevista nas notas desta proposta.")
        pdf.multi_cell(0, 6, f"b) Horas tecnicas alocadas: {horas_tecnicas} horas.")
        pdf.multi_cell(0, 6, f"c) Forma de Pagamento: A vista ou em ate {parcelas} parcelas mensais, iguais e consecutivas.")
        pdf.multi_cell(0, 6, f"d) Prazo para finalizacao: 60 dias.")
        pdf.ln(5)

        # 5. Notas
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Notas", ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 6, "Esta proposta tem validade de 3 dias uteis.")

        # Rodapé
        pdf.set_y(-25)
        pdf.set_font("Arial", 'I', 8)
        pdf.cell(0, 5, razao_social.upper(), ln=True, align='C')
        pdf.cell(0, 5, "PROPOSTA DE TRABALHO - Pagina 2 de 2", ln=True, align='C')

        # Geração do arquivo
        try:
            pdf_output = bytes(pdf.output())
        except TypeError:
            pdf_output = pdf.output(dest='S').encode('latin-1')

        st.success("Cálculo realizado com sucesso!")
        st.download_button(
            label="📥 Baixar Proposta em PDF",
            data=pdf_output,
            file_name=f"Proposta_RPC_{razao_social}.pdf",
            mime="application/pdf",
            type="primary"
        )