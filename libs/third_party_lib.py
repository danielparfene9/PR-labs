from fastapi import FastAPI, UploadFile, File, HTTPException, Path
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Query
from pydantic import BaseModel, HttpUrl, Field
from contextlib import asynccontextmanager
from typing import List, Optional
import uvicorn