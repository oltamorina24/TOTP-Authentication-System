# TOTP-Authentication-System

Ky projekt implementon një sistem autentikimi me dy faktorë (**2FA**) duke përdorur kodet **TOTP** (Time-based One-Time Password). Sistemi përdor një arkitekturë Client-Server për të verifikuar përdoruesit përmes një kanali të enkriptuar.

---

## Struktura e Projektit

Projekti përbëhet nga pesë skedarë kryesorë:

* **`server.py`**: Menaxhon lidhjet hyrëse, dekripton të dhënat dhe kryen verifikimin e kodit.
* **`client.py`**: Ndërfaqja ku përdoruesi jep emrin dhe kodin TOTP për t'u dërguar te serveri.
* **`security.py`**: Përmban logjikën e enkriptimit me Fernet dhe gjenerimin/verifikimin e TOTP përmes PyOTP.
* **`users.py`**: Shërben si një "database" e thjeshtë me emrat e përdoruesve dhe çelësat e tyre sekretë.
* **`logger.py`**: Regjistron çdo tentativë për kyçje (SUCCESS/FAILED) në skedarin `logs.txt`.

---

## Kërkesat dhe Instalimi

Për të ekzekutuar këtë projekt, duhet të keni Python të instaluar dhe bibliotekat e mëposhtme:

1.  Hap terminalin në VS Code.
2.  Instalo varësitë me këtë komandë:
    ```bash
    pip install pyotp cryptography
    ```

---

## Si të përdoret sistemi

Ndiqni këto hapa për të testuar autentikimin:

1.  **Nisni Serverin:**
    Ekzekutoni skedarin e serverit që të fillojë dëgjimin në portën 5000.
    ```bash
    python server.py
    ```
2.  **Nisni Klientin:**
    Në një dritare të re terminali, ekzekutoni klientin.
    ```bash
    python client.py
    ```
3.  **Procesi i Logimit:**
    * Shtypni një nga emrat e përdoruesve (p.sh., `alice`, `bob`, ose `admin`).
    * Programi do t'ju shfaqë kodin TOTP që "pajisja juaj 2FA" po gjeneron për momentin.
    * Shkruani atë kod dhe do të merrni përgjigjen nga serveri nëse qasja u lejua.

---

## Siguria e Implementuar

* **Enkriptimi:** Të dhënat dërgohen si "payload" i enkriptuar duke përdorur çelësin simetrik `ENCRYPTION_KEY` të definuar në `security.py`.
* **Validimi:** Serveri përdor një dritare kohore (`valid_window=1`) për të lejuar sinkronizimin e kodit edhe nëse ka vonesa të vogla kohore.
* **Auditimi:** Çdo veprim regjistrohet me timestamp në një skedar log-u për monitorim të mëvonshëm.