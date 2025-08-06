{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fc7a213e-dda7-4046-a4ae-18ecb927f431",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (159709101.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[4], line 2\u001b[1;36m\u001b[0m\n\u001b[1;33m    pip install fastapi\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# qoe_api.py\n",
    "pip install fastapi \n",
    "from fastapi import FastAPI\n",
    "from fastapi.middleware.cors import CORSMiddleware\n",
    "from random import uniform, randint\n",
    "import uvicorn\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "app.add_middleware(\n",
    "    CORSMiddleware,\n",
    "    allow_origins=[\"*\"], allow_credentials=True,\n",
    "    allow_methods=[\"*\"], allow_headers=[\"*\"],\n",
    ")\n",
    "\n",
    "@app.get(\"/qoe\")\n",
    "def get_qoe():\n",
    "    return {\n",
    "        \"playback_time\": round(uniform(10, 100), 2),\n",
    "        \"loaded_fraction\": round(uniform(0.4, 1.0), 2),\n",
    "        \"buffering_events\": randint(0, 3),\n",
    "        \"playing_events\": randint(1, 5),\n",
    "        \"bitrate\": round(uniform(1000, 5000), 1),  # kbps\n",
    "    }\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    uvicorn.run(app, host=\"127.0.0.1\", port=8000)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "275a9446-3f51-4996-a80e-24cd82aef980",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
