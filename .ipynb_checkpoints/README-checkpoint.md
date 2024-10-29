# networks-project
Project repository for Graduate computer networks at UVA 

# Setup Guide (Windows, Sorry Mateen)

# Instructions for Setting Up and Running a Jupyter Notebook in a QEMU VM

## Step 1: Download QEMU
   - **Choose your installation method** based on your environment:
     - **For WSL2**: Use the \`apt\` package manager.
       ```bash
       sudo apt update
       sudo apt install qemu qemu-kvm
       ```
     - **For MSYS**: Follow the instructions at [MSYS2 Official Site](https://www.msys2.org/).
   - Ensure QEMU is properly installed and accessible by running:
     ```bash
     qemu-system-x86_64 --version
     ```

## Step 2: Download the QEMU Image
   - Download the pre-configured QEMU image from [this link](https://polybox.ethz.ch/index.php/s/QlrfHm7uYw6vISe).
   - Save the \`.qcow2\` image file to a location where you can easily access it.

## Step 3: Launch the QEMU VM with Port Forwarding
   - Run the QEMU image, ensuring to set up port forwarding so that Jupyter Notebook can be accessed from your local machine:
     ```bash
     qemu-system-x86_64 -drive file=path/to/your-image.qcow2,format=qcow2 -m 2048 \\
         -net user,hostfwd=tcp::8888-:8888 -net nic
     ```
   - Replace \`path/to/your-image.qcow2\` with the actual path to your downloaded \`.qcow2\` file.

## Step 4: Set Up JupyterLab in the QEMU VM
   - Once logged into the VM, **install JupyterLab** using \`pip\`:
     ```bash
     pip install jupyterlab
     ```
   - **Clone the required repository** into the VM if any specific codebase or resources are needed for your project:
     ```bash
     git clone <repository-url>
     ```

## Step 5: Start JupyterLab
   - Run JupyterLab within the VM:
     ```bash
     jupyter-lab --no-browser --ip=0.0.0.0 --port=8888
     ```
   - You should see a URL with a token in the output (like \`http://127.0.0.1:8888/lab?token=<token>\`).
   - On your host machine, **open a browser** and go to:
     ```
     http://localhost:8888/lab?token=<token>
     ```
   - Replace \`<token>\` with the authentication token provided in the terminal output.

   